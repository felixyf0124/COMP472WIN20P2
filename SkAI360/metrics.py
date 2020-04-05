
class Metrics:

    def __init__(self):
        self.statistics = self.instMetricEntry()
        self.correct = 0
        self.wrong = 0
        self.analysis = dict()

    # instancing a metric entry
    def instMetricEntry(self):
        entry = dict()
        keys = {"eu", "ca", "gl", "es", "en", "pt"}
        # detected language
        for detected in keys:
            entry[detected] = dict()
            # target language
            for target in keys:
                entry[detected][target] = 0
        return entry

    # update metrics statistical data table
    def update(self, detectedLan: str, targetLan: str):
        self.statistics[detectedLan][targetLan] += 1
        if(targetLan == detectedLan):
            self.correct += 1
        else:
            self.wrong += 1

    # do analyze
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

    # return accuracy
    def getAccuracy(self):
        if("accuracy" not in self.analysis):
            self.analyze()
        return self.analysis.get("accuracy")

    # calculate and return precision for specific language class
    def getPrecision(self, language: str):
        tp = self.statistics[language][language]
        keys = {"eu", "ca", "gl", "es", "en", "pt"}
        predictTotal = 0
        for key in keys:
            predictTotal += self.statistics[language][key]
        if(predictTotal != 0):
            precision = tp / predictTotal
        else:
            precision = str(tp) + "/0"
        return precision

    # calculate and return recall for specific language
    def getRecall(self, language: str):
        tp = self.statistics[language][language]
        keys = {"eu", "ca", "gl", "es", "en", "pt"}
        actualTotal = 0
        for key in keys:
            actualTotal += self.statistics[key][language]
        if(actualTotal != 0):
            recall = tp / actualTotal
        else:
            recall = str(tp) + "/0"
        return recall

    # calculate and return F1-measure for specific language
    def getF1Measure(self, language: str, precision=None, recall=None):
        if(precision != None) & (recall != None):
            p = precision
            r = recall
        else:
            p = self.getPrecision(language)
            r = self.getRecall(language)

        if(type(p) is str) | (type(r) is str):
            f_measure = "None"
        elif(p+r == 0):
            f_measure = "None"
        else:
            f_measure = 2*p*r/(p+r)
        return f_measure

    # return macro F1 average
    def getMacroF1(self):
        total = 0.0
        count = 0
        for key in self.analysis["f1Measure"]:
            if(type(self.analysis["f1Measure"][key]) is float):
                total += self.analysis["f1Measure"][key]
                count += 1
            # else:
            #     return "None"
        average = total/count
        return average

    # return F1 weighted average
    def getWeightedAverageF1(self):
        total = 0
        sumActualTotal = 0
        keys = {"eu", "ca", "gl", "es", "en", "pt"}
        for each in self.analysis["f1Measure"]:
            f1 = self.analysis["f1Measure"][each]
            if(type(f1) is float):
                actualTotal = 0
                for key in keys:
                    actualTotal += self.statistics[key][each]
                total += f1 * actualTotal
                sumActualTotal += actualTotal
            # else:
            #     return "None"
        weightedAve = total/sumActualTotal
        return weightedAve

    # return analysis result
    def getAnalysisResult(self):
        return self.analysis
