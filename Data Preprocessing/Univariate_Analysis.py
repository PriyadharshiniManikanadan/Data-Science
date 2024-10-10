class Univariate():
    
# quanQual Seperation 
    
    def quanQual(dataset):
        qual = []
        quan = []
        for columnName in dataset.columns:
            #print(columnName)
            if dataset[columnName].dtype == 'object':
                #print("qual")
                qual.append(columnName)
            else:
                #print("quan")
                quan.append(columnName)
        return quan,qual

    
# Central Tendency, Percentile, IQR, Skewness, Kurtosis
    
    def Univariate(dataset,quan):
        descriptive = pd.DataFrame(index=['Mean', 'Median', 'Mode', 'Q1:25%', 'Q2:50%', "Q3:75%", "99%", "Q4:100%",
                                      "IQR", "1.5-Rule", "Lesser_Outlier", "Greater_Outlier", "Min", "Max", "Skew", "Kurtosis"], columns = quan)
        for columnName in quan:
            descriptive[columnName]['Mean'] = dataset[columnName].mean()    
            descriptive[columnName]['Median'] = dataset[columnName].median()
            descriptive[columnName]['Mode'] = dataset[columnName].mode()[0]     
            descriptive[columnName]['Q1:25%'] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]['Q2:50%'] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]['Q3:75%'] = dataset.describe()[columnName]["75%"]
            descriptive[columnName]['99%'] = np.percentile(dataset[columnName],99)
            descriptive[columnName]['Q4:100%'] = dataset.describe()[columnName]["max"]
            descriptive[columnName]['IQR'] = descriptive[columnName]['Q3:75%'] - descriptive[columnName]['Q1:25%']
            descriptive[columnName]['1.5-Rule'] = 1.5 * descriptive[columnName]['IQR']
            descriptive[columnName]['Lesser_Outlier'] = descriptive[columnName]['Q1:25%'] - descriptive[columnName]['1.5-Rule']
            descriptive[columnName]['Greater_Outlier'] = descriptive[columnName]['Q3:75%'] + descriptive[columnName]['1.5-Rule']
            descriptive[columnName]['Min'] = dataset[columnName].min()
            descriptive[columnName]['Max'] = dataset[columnName].max()
            descriptive[columnName]['Skew'] = dataset[columnName].skew()
            descriptive[columnName]['Kurtosis'] = dataset[columnName].kurtosis()
        return descriptive    

    
# Finding Outlier columns

    def CheckOutliers(quan):
        Lesser = []
        Greater = []
        for columnName in quan:
            if Descriptive[columnName]['Min'] < Descriptive[columnName]['Lesser_Outlier']:
                Lesser.append(columnName)
            if Descriptive[columnName]['Max'] > Descriptive[columnName]['Greater_Outlier']:
                Greater.append(columnName)
        return CheckOutliers
       

# Replace Outliers

    def ReplaceOutliers(dataset,columnName):
        for columnName in Lesser:
            dataset[columnName][dataset[columnName]<Descriptive[columnName]['Lesser_Outlier']] = Descriptive[columnName]['Lesser_Outlier']
        
        for columnName in Greater:
            dataset[columnName][dataset[columnName]>Descriptive[columnName]['Greater_Outlier']] = Descriptive[columnName]['Greater_Outlier']
        return ReplaceOutliers

    
# Frequency, Relative Frquency, Cumulative Frequency

    def FreqTable(columnName,dataset):
        FreqTable = pd.DataFrame(columns = ["Unique_Values", "Frequency", "Relative_Frequency", "Culmulative_Frequency"])    
        FreqTable["Unique_Values"] = dataset[columnName].value_counts().index
        FreqTable["Frequency"] = dataset[columnName].value_counts().values
        FreqTable["Relative_Frequency"] = (FreqTable["Frequency"]/103)                          
        FreqTable["Culmulative_Frequency"] = FreqTable["Relative_Frequency"].cumsum()
        return FreqTable
                
