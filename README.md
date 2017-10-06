# Parallel channel/lumen radius calculator

## Usage
1. change to bash shell by typing `bash`
2. add my environment variables to your bash shell `bashrc`.
   This provides you a `module` command to load softwares
   installed in my directory.
3. load python-3 and HOLE into to your bash shell
   ```bash
    module add conda
    module add hole
    ```
4. use VMD to save all the frames (with selected atoms) into a folder.
5. modify the `template.hole.yaml` file to suit your need
6. generate a `hole.yaml` file containing all you input pdb files.
   ```bash
   python series.py template.hole.yaml task.yaml
   ```
7. run `umolhole hole.yaml`.
   You should see three output files in the target folder 
   as you specified in `hole.yaml`.

#### Info.
* author: Yuhang(Steven) Wang
* date: 10/6/2017




