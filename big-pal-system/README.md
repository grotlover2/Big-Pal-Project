# Big Pal System
This is the core game logic system that implements the dynamic weight gain system used to adjust the size of the pals according to their hunger level. This mod makes use of UE blue prints to implement the logic and [UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) to inject it at runtime. The modding API is provided by the [PalworldModdingKit](https://github.com/localcc/PalworldModdingKit).

## Install
In general you can follow the instructions on the [PalWorld Modding Wiki](https://pwmodding.wiki/docs/palworld-modding-kit/install-part-1). The main things is to ensure you have the prerequisites installed and you properly install the Wwise plugin.

### Known Issues
- When opening for the first time it will prompt to you recompile. Sometimes this fails and requires to be opened and recompiled again.
- Sometimes the project fails to rebuild due to failing to build the `CapsuleTraceRotation` plugin under the `EnginePlugins` directory. I do not know what causes this but may be a BOM or formatting issue with the source code. Copying the files to another directory and then back seems to fix it.

## How Does it Work?
The main blue print is `ModActor` under `Content/Mods/PalWgSystem`. This blueprint is loaded at game start and runs two major routines every tick, `Process Pal Monsters` and `Process Funnel Pals`. The following is a list of some of the functions and routines along with a descirption of what they do.

### Process Pal Monsters
This routine looks for all pals that have been spawned then sets their shape key according to the default if they are wild, or to the value defined in the gain curve according to their hunger if they are caught.

### Process Funnel Pals
This routine is very simular to `Process Pal Monsters` but instead works on what are called 'Funnel Pals'. The game defines 'Funnel Pals' at the pals that float around the player when an item is equiped.

### SetPal Size
This function takes in a pal and a Morph Target and then figures the value that should be passed to `SetPal Size Morph Target` based on the Pals current hunger.

### GetFatMorph Target
This function looks at the gender of the pal and determins which morph target should be used, either `MaleFatMorphTarget` or `FemaleFatMorphTarget`.

### SetPal Size Morph Target
This function sets the shape key on the pal according to the passed morph target and value that is then used to get how fat the pal should be from the `GainCurve`.

### SetPal Size
This function just s

## Blue Print Configutation
The system makes use of a small handfull of variables set on the blue print for general configuration.

- `DefaultPalSize` - The default size all pals should be. Adjust this to make wild pals bigger or smaller.
- `FatMorphTarget` - Name of the Fat Shape Key. **Should not be changed**
- `MaleFatMorphTarget` - Name of the Male Fat Shape Key. **Should not be changed**
- `FemaleFatMorphTarget` - Name of the Female Fat Shape Key. **Should not be changed**
- `GainCurve` - This is a curve defined in the `GainCurve` resource under `Content/Mods/PalWgSystem`. **Should not be changed**

## Gain Curve
The Gain Curve is a resource defined under `Content/Mods/PalWgSystem`. This curve can be adjusted to adjust how quickly pals gain or lose weight realtive to their hunger.