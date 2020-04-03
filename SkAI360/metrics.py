
class Metrics:

    def __init__(self):
        self.statistics = dict()
        self.statistics["eu"] = self.instMetricEntry()
        self.statistics["ca"] = self.instMetricEntry()
        self.statistics["gl"] = self.instMetricEntry()
        self.statistics["es"] = self.instMetricEntry()
        self.statistics["en"] = self.instMetricEntry()
        self.statistics["pt"] = self.instMetricEntry()
        self.correct = 0
        self.wrong = 0
        self.analysis = dict()

    def instMetricEntry(self):
        entry = dict()
        entry["TP"] = 0  # true positive
        entry["FP"] = 0  # false positive
        entry["FN"] = 0  # false negative
        entry["actualTotal"] = 0
        return entry

    def update(self, targetLan: str, detectedLan: str):
        if(targetLan == detectedLan):
            self.statistics[targetLan]["TP"] += 1
            self.correct += 1
        else:
            self.statistics[targetLan]["FN"] += 1
            self.statistics[detectedLan]["FP"] += 1
            self.wrong += 1
        self.statistics[targetLan]["actualTotal"] += 1

    def analyze(self):
        self.analysis["accuracy"] = self.correct / (self.correct+self.wrong)
        self.analysis["precision"] = dict()
        self.analysis["recall"] = dict()
        self.analysis["f1Measure"] = dict()
        for key in self.statistics:
            p = self.getPrecision(key)
            r = self.getRecall(key)
            self.analysis["precision"][key] = p
            self.analysis["recall"][key] = r
            self.analysis["f1Measure"][key] = self.getF1Measure(key, p, r)
        self.analysis["macroF1"] = self.getMacroF1()
        self.analysis["weightedAverageF1"] = self.getWeightedAverageF1()

    # calculate and return precision for specific language

    def getPrecision(self, language: str):
        tp = self.statistics[language]["TP"]
        fp = self.statistics[language]["FP"]
        precision = tp / (tp + fp)
        return precision

    # calculate and return recall for specific language
    def getRecall(self, language: str):
        tp = self.statistics[language]["TP"]
        fn = self.statistics[language]["FN"]
        recall = tp / (tp + fn)
        return recall

    # calculate and return F1-measure for specific language
    def getF1Measure(self, language: str, precision=None, recall=None):
        if(precision != None & recall != None):
            p = precision
            r = recall
        else:
            p = self.getPrecision(language)
            r = self.getRecall(language)
        f_measure = 2*p*r/(p+r)
        return f_measure

    # return macro F1 average
    def getMacroF1(self):
        total = 0
        for key in self.analysis["f1Measure"]:
            total += self.analysis["f1Measure"][key]
        average = total/len(self.analysis["f1Measure"])
        return average

    # return F1 weighted average
    def getWeightedAverageF1(self):
        total = 0
        for key in self.analysis["f1Measure"]:
            f1 = self.analysis["f1Measure"][key]
            actualTotal = self.statistics[key]["actualTotal"]
            total += f1 * actualTotal
        weightedAve = total/(self.correct + self.wrong)
        return weightedAve

    # return analysis result
    def getAnalysisResult(self):
        return self.analysis
