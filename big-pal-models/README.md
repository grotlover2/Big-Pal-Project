# Big Pal Models
This project holds all the modifed models for the Big Pal Project

## Getting started
1. Clone or download this repo
  - Note: If using git make sure you have git lfs installed for the fbx files
2. Make sure under `Project Settings` that `Generate Chunks` and `Cook Everything` are checked
  - These should be set already but good to double check

## Directory Structure
- Models - This folder holds the fbxs and optionally any blend files
- Pal/Pal - The main project directory
  - Mod - The main mod output folder. Also holds the UnrealPak tools
  - dbg - The indivdual pak files for testing
  - UnrealPak - The UnrealPak tools

## Editor python scripts
I have a python script that is used to help bulk process and pack the models. It handles processing
the models so they match the naming and directory conventions as well as creating both a combined
and individual pak for all the pals.

### Script Setup
1. Under `Project Settings` go to `Plugins` and look for `Python`
2. Ensure that `Developer Mode` is checked
  - Might be under the Advanced section
  - Might already be enabled 
3. When you open up the editor go to `Output Log` and ensure the command entry is set to Python
4. Run `import pak_tools as PT` to give the tools script an alias to call
  - You will need to do this every time you open up the project

### Process Models
1. Under `Content/Pal/Model/Character/Monster` create a new folder that matches the name of the
   pal you are adding in, or use the exsiting one if available
2. Drag in your fbx file to import it
3. Once imported clean out any animations or other assets that could cause problems
4. Save all and run `PT.process_models()`. This will rename the files and move the skeltons to 
   the skeleton directory
5. Save all again to be safe

### Creating Paks
1. Go to `Platforms` and cook the project for windows
2. Once the project is cooked run `PT.build_pak()` to build all the pak files
