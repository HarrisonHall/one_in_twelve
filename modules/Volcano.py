class Volcano:
    def __init__(self,csvrow):
        self.name = csvrow[0]
        maxl = len(csvrow)
        try:
            self.latitude = float(csvrow[maxl-1].replace("\t",""))
            self.longitude = float(csvrow[maxl-2].replace("\t",""))
            self.elevation = float(csvrow[maxl-3].replace("\t",""))
        except:
            self.name = None

