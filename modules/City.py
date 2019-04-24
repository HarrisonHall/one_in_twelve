class City:
    def __init__(self,csvrow):
        self.name = csvrow[0]
        self.latitude = float(csvrow[2])
        self.longitude = float(csvrow[3])
        self.population = int(float(csvrow[9]))

