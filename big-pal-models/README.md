# Big Pal Models
This project holds all the modifed models for the Big Pal Project and produces the model replacement pak.

## Getting started
1. Clone or download the `Big-Pal-Project` repo
  - Note: If using git make sure you have git lfs installed for the fbx files
2. Make sure under `Project Settings` that `Generate Chunks` and `Cook Everything` are checked
  - These should be set already but good to double check

## Directory Structure
- Models - This folder holds the fbxs and optionally any blend files
- Pal/Pal - The main project directory
  - Mod - The main mod output folder. Also holds the UnrealPak tools
  - dbg - The indivdual pak files for testing
  - UnrealPak - The UnrealPak tools

## Making Pals Able to Gain Weight
The `big-pal-system` dynamically adjust the size of pals by setting one or more shape keys **(aka morph targets)** on the pals model if they are present to a value between 0.0 (thin) and 1.0 (fat). To allow the system to interact with a pal the model needs to be modified to have the expected shape keys.

### Shape Keys
- **Fat** - This shape key is always set if present on the model. This key acts like a default or shared morph
that should be applied to a pal regardless of gender. Meant mainly for if both the male and female version of the pal have the same morph or if `FatMale` and/or `FatFemale` keys are used to modify a base morph.
- **FatMale** - This shape key is set only if the pal's gender is male or not set. This key is meant mainly
for any specalized morphs that should only be applied to male pals.
- **FatFemale** - This shape key is set only if the pal's gender is female. This key is meant mainly for any
specalized morphs that should only be applied to female pals. 

## Adding Modified Models to the Game
The `Big Pal Project` uses the [asset swapping method](https://pwmodding.wiki/docs/category/asset-swapping) to replace the pals models with ones that the `big-pal-system` can interact with. This process abuses Unreals patching mechinism to replace the pal models with the modded ones. This means the directory structure needs to be an exact mimimic of the one setup in the base palworld game.

To help ease the process a bit I have a python script that is used to help bulk process and pack the models. It handles processing the models so they match the naming and directory conventions as well as creating both a combined and individual pak for all the pals.

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
   pal you are adding in **(NOTE: This is the pals INTERNAL NAME, not their display name!)**, or use the exsiting one if available
2. Drag in your fbx file to import it
3. Once imported clean out any animations or other assets that could cause problems
4. Save all and run `PT.process_models()`. This will rename the files and move the skeltons to 
   the skeleton directory
5. Save all again to be safe
6. Add an entry for the pal to `pak_config.py` using the pals internal name (same as what the directory should be) and have `release` set to `False` (assuming it does not already exsist).

### Marking a Model Ready for Release
The `pak_tools.py` script makes use of a config in `pak_config.py` to mark what pals need to be packed and if
they are ready for release or not. If `release` is not set to `True` for that pal when `PT.build_pak()` is run
it will not add that pal into the final condensed pak and only build the individual debug pak found in the `dbg` folder.

### Creating Paks
1. Go to `Platforms` and cook the project for windows
2. Once the project is cooked run `PT.build_pak()` to build all the pak files
