from utils.generation import Generation
from utils.reading import Reading
from utils.deletion import Deletion

reading = Reading('1g26kdbYZs_1Uvx862dZ37bK1Xa1u62HaFqpIzsdy9xI')
generation = Generation('1g26kdbYZs_1Uvx862dZ37bK1Xa1u62HaFqpIzsdy9xI')
deletion = Deletion('1g26kdbYZs_1Uvx862dZ37bK1Xa1u62HaFqpIzsdy9xI')

print(reading.get_by_keyword(['English', 'Math'], 'Sample Data'))