#!/usr/bin/env python
"""
Repeat ether the whole text or line by line
    (:1:), (:2:), ... for the whole text
    [:1:], [:2:], ... for lines
usage: series template.addWater.yaml params.yaml
    The output is "addWater.yaml".
Author: Yuhang(Steven) Wang
Date: 04/17/2017
Update: 05/12/2017
License: MIT/X11
"""
from typing import List
import re
import sys
import yaml
import json
import itertools
from functools import reduce


def replace_line_by_line(input_str: str, params: list, pattern: str) -> list:
    """Replace each line by the substitutes in params"""
    def aux(s: str):
        if re.search(pattern, s):
            return replace_whole(s, params, pattern)
        else:
            return s

    return "\n".join(map(aux, input_str.split("\n")))


def  flatten_list(ls: List[list]) -> list:
    return list(itertools.chain(*ls))


def replace_whole(s: str, params: list, pattern: str) -> str:
    """
    Replace the whole content
    """
    def aux(p: list, accum: list) -> str:
        if len(p) == 0:
            return "\n".join(accum)
        elif isinstance(p[0], str) and re.match(r"\d+-\d+", p[0]):
            start, stop = [int(x) for x in p[0].split("-")]
            return aux(
                p[1:],
                accum + [re.sub(pattern, str(i), s) for i in range(start, stop+1)])
        else:
            return aux(p[1:], accum + [re.sub(pattern, str(p[0]), s)])

    if len(params) == 0:
        return s
    else:
        return aux(params, [])


def main_replace(s: str, ps: list, counter: int = 1) -> str:
    pattern = "\(:{}:\)".format(counter)
    if len(ps) == 0:
        return s
    else:
        return main_replace(
            replace_whole(s, ps[0], pattern),
            ps[1:],
            counter + 1
        )


def sub_replace(s: str, ps: list, counter: int = 1) -> str:
    pattern = "\[:{}:\]".format(counter)
    if len(ps) == 0:
        return s
    else:
        return sub_replace(
            replace_line_by_line(s, ps[0], pattern),
            ps[1:],
            counter + 1
        )


def work(s: str, p: dict) -> str:
    if "main" in p:
        return work(
            main_replace(s, p["main"]),
            {k: v for k, v in p.items() if k != "main"},
        )
    elif "sub" in p:
        return sub_replace(s, p["sub"])
    else:
        return s


def savetxt(f_out: str, content: str):
    with open(f_out, 'w') as OUT:
        OUT.write(content)


def main(args: List[str]):
    template = args[0]
    out_prefix = template.replace("template.","").replace(".yaml", "")
    file_params = args[1]
    with open(file_params, "r") as IN:
        params = yaml.load(IN)
    with open(template, 'r') as IN:
        content = IN.read()
    new_content = work(content, params)
    print(new_content)
    f_yaml = "{}.yaml".format(out_prefix)
    savetxt(f_yaml, new_content)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error hint: Need 2 arguments")
        exit()
    main(sys.argv[1:])
