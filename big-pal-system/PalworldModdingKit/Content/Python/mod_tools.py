import os
import pathlib
import shutil

import unreal

PALWORLD_PAK_DIR = pathlib.Path('F:/SteamLibrary/steamapps/common/Palworld/Pal/Content/Paks')

PROJECT_DIR = pathlib.Path(unreal.Paths.get_project_file_path()).parent.absolute().resolve()
PAK_DIR = f'{PROJECT_DIR}/out/Windows/Pal/Content/Paks'


def rename_pak():
    mod_name, chunk_id = _get_mod_info()
    pak_file = pathlib.Path(f'{PAK_DIR}/pakchunk{chunk_id}-Windows.pak')
    if not pak_file.exists():
        unreal.log_error(f'Missing {pak_file}, make sure to pake your project before running this script.')
        return

    mod_pak = pathlib.Path(f'{PAK_DIR}/{mod_name}.pak')
    unreal.log(f'Renaming {mod_name} to {mod_pak}...')
    shutil.move(pak_file, mod_pak)
    unreal.log(f'Renamed {mod_name} to {mod_pak}')


def install_pak():
    mod_name, chunk_id = _get_mod_info()
    mod_pak_path = pathlib.Path(f'{PAK_DIR}/{mod_name}.pak')
    if not mod_pak_path.exists():
        rename_pak()

    pak_install_dir = pathlib.Path(f'{PALWORLD_PAK_DIR}/LogicMods/{mod_name}.pak')
    unreal.log(f'Copying mod to {pak_install_dir}...')
    if pak_install_dir.exists():
        unreal.log_warning(f'{pak_install_dir} exists, removing...')
        os.remove(pak_install_dir)
    shutil.copy(mod_pak_path, pak_install_dir)
    unreal.log(f'Done installing mod to {pak_install_dir}')


def _get_mod_info():
    eal = unreal.EditorAssetLibrary()
    asset_label = eal.load_asset('/Game/Label_PalWgSystem')
    mod_name = asset_label.get_name().split('_')[1]
    chunk_id = asset_label.get_editor_property("rules").get_editor_property('ChunkId')

    return mod_name, chunk_id
