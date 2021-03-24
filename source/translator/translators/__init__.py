from pathlib import Path
from glob import glob


__all__ = [module_name.split('/')[-1].split('.')[0] for module_name in glob(f'{Path(__file__).parent.absolute()}/*')]