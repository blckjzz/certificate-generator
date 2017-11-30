from os.path import join, dirname
from dotenv import load

dotenv_path = join(dirname(__file__), '.env')
load(dotenv_path, verbose=True)

load(find_dotenv())


