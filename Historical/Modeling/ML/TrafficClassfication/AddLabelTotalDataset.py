# -------------------------------- Import Libraries
import pandas as pd

# -------------------------------- Read CSV
data = pd.read_csv('total_data.csv')

# Function to calculate the Total, BusCount, TruckCount, and update the Traffic_Situation column in the CSV file
class Addlabel:
    def AddLabel(self, data):
        # Calculate the maxBus, maxTruck, and maxTotal using the FindMax class
        maxTotalRoad1 = FindMax().FindMaxTotalRoad1(data)
        maxTotalRoad2 = FindMax().FindMaxTotalRoad2(data)
        maxBusRoad1 = FindMax().FindMaxBusRoad1(data)
        maxBusRoad2 = FindMax().FindMaxBusRoad2(data)
        maxTruckRoad1 = FindMax().FindMaxTruckRoad1(data)
        maxTruckRoad2 = FindMax().FindMaxTruckRoad2(data)

        # print(int((75 / 100) * maxTotal))

        # Update the "Traffic_Situation" column based on the "Total", 'BusCount', 'Truck_Count' columns
        for index, row in data.iterrows():
            # Define the variable to access the columns
            TotalRoad1 = row['TotalRoad1']
            TotalRoad2 = row['TotalRoad2']
            BusRoad1 = row['BusRoad1']
            BusRoad2 = row['BusRoad2']
            TruckRoad1 = row['TruckRoad1']
            TruckRoad2 = row['TruckRoad2']

            # ----------------------------------------------- Heavy --------------------------------------
            # Check the heavy traffic for both side
            if TotalRoad1 > int((80 / 100) * maxTotalRoad1) and TotalRoad2 > int((80 / 100) * maxTotalRoad2):
                data.at[index, 'Traffic Situation'] = 'BothSideHeavy'

            # check the heavy traffic for Road1
            elif TotalRoad1 > int((80 / 100) * maxTotalRoad1) and TotalRoad2 < int((80 / 100) * maxTotalRoad2):
                if BusRoad2 > int((80 / 100) * maxBusRoad2) or TruckRoad2 > int((80 / 100) * maxTruckRoad2):
                    data.at[index, 'Traffic Situation'] = 'BothSideHeavy'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side1Heavy'
            # Check the heavy traffic for Road2
            elif TotalRoad2 > int((80 / 100) * maxTotalRoad2) and TotalRoad1 < int((80 / 100) * maxTotalRoad1):
                if BusRoad1 > int((80 / 100) * maxBusRoad1) or TruckRoad1 > int((80 / 100) * maxTruckRoad1):
                    data.at[index, 'Traffic Situation'] = 'BothSideHeavy'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side2Heavy'

            # --------------------------------------------------< High >-----------------------------------------------------------

            # Check the high traffic for both side
            elif int((60 / 100) * maxTotalRoad1) < TotalRoad1 < int((80 / 100) * maxTotalRoad1) and int((60 / 100) * maxTotalRoad2) < TotalRoad2 < int((80 / 100) * maxTotalRoad2):
                data.at[index, 'Traffic Situation'] = 'BothSideHigh'

            # check the high traffic for Road1
            elif int((60 / 100) * maxTotalRoad1) < TotalRoad1 < int((80 / 100) * maxTotalRoad1) and TotalRoad2 < int((60 / 100) * maxTotalRoad2):
                if BusRoad2 > int((60 / 100) * maxBusRoad2) or TruckRoad2 > int((60 / 100) * maxTruckRoad2):
                    data.at[index, 'Traffic Situation'] = 'BothSideHigh'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side1High'

            # Check the high traffic for Road2
            elif int((60 / 100) * maxTotalRoad2) < TotalRoad2 < int((80 / 100) * maxTotalRoad2) and TotalRoad1 < int((60 / 100) * maxTotalRoad1):
                if BusRoad1 > int((60 / 100) * maxBusRoad1) or TruckRoad1 > int((60 / 100) * maxTruckRoad1):
                    data.at[index, 'Traffic Situation'] = 'BothSideHigh'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side2High'
            # --------------------------------------------------< Normal >---------------------------------------------
            # Check the high traffic for both side
            elif int((40 / 100) * maxTotalRoad1) < TotalRoad1 < int((60 / 100) * maxTotalRoad1) and int((40 / 100) * maxTotalRoad2) < TotalRoad2 < int((60 / 100) * maxTotalRoad2):
                data.at[index, 'Traffic Situation'] = 'BothSideNormal'

            # check the high traffic for Road1
            elif int((40 / 100) * maxTotalRoad1) < TotalRoad1 < int((60 / 100) * maxTotalRoad1) and TotalRoad2 < int((40 / 100) * maxTotalRoad2):
                if BusRoad2 > int((40 / 100) * maxBusRoad2) or TruckRoad2 > int((40 / 100) * maxTruckRoad2):
                    data.at[index, 'Traffic Situation'] = 'BothSideNormal'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side1Normal'

            # Check the high traffic for Road2
            elif int((40 / 100) * maxTotalRoad2) < TotalRoad2 < int((60 / 100) * maxTotalRoad2) and TotalRoad1 < int((40 / 100) * maxTotalRoad1):
                if BusRoad1 > int((40 / 100) * maxBusRoad1) or TruckRoad1 > int((40 / 100) * maxTruckRoad1):
                    data.at[index, 'Traffic Situation'] = 'BothSideNormal'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side2Normal'
            # --------------------------------------------------< Low >------------------------------------------------
            # Check the Low traffic for both side
            elif int((1 / 100) * maxTotalRoad1) < TotalRoad1 < int((40 / 100) * maxTotalRoad1) and int((1 / 100) * maxTotalRoad2) < TotalRoad2 < int((40 / 100) * maxTotalRoad2):
                data.at[index, 'Traffic Situation'] = 'BothSideLow'

            # check the Low traffic for Road1
            elif int((1 / 100) * maxTotalRoad1) < TotalRoad1 < int((40 / 100) * maxTotalRoad1) and TotalRoad2 > int((40 / 100) * maxTotalRoad2):
                if BusRoad1 > int((40 / 100) * maxBusRoad1) or TruckRoad1 > int((40 / 100) * maxTruckRoad1):
                    data.at[index, 'Traffic Situation'] = 'BothSideNormal'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side1Low'

            # Check the Low traffic for Road2
            elif int((1 / 100) * maxTotalRoad2) < TotalRoad2 < int((40 / 100) * maxTotalRoad2) and TotalRoad1 > int((40 / 100) * maxTotalRoad1):
                if BusRoad2 > int((40 / 100) * maxBusRoad2) or TruckRoad2 > int((40 / 100) * maxTruckRoad2):
                    data.at[index, 'Traffic Situation'] = 'BothSideNormal'
                else:
                    data.at[index, 'Traffic Situation'] = 'Side2Low'
            # # Save the updated data back to the CSV file
            data.to_csv('total_data.csv', index=False)


# Class used for finding the max values
class FindMax:
    def FindMaxTotalRoad1(self, data):
        maxTotalRoad1 = data['TotalRoad1'].max()
        return maxTotalRoad1
    def FindMaxTotalRoad2(self, data):
        maxTotalRoad2 = data['TotalRoad2'].max()
        return maxTotalRoad2

    def FindMaxBusRoad1(self, data):
        maxBusRoad1 = data['BusRoad1'].max()
        return maxBusRoad1
    def FindMaxBusRoad2(self, data):
        maxBusRoad2 = data['BusRoad2'].max()
        return maxBusRoad2
    def FindMaxTruckRoad1(self, data):
        maxTruckRoad1 = data['TruckRoad1'].max()
        return maxTruckRoad1
    def FindMaxTruckRoad2(self, data):
        maxTruckRoad2 = data['TruckRoad2'].max()
        return maxTruckRoad2

# Create an instance of the Addlabel class
add_label = Addlabel()

# Call the AddLabel method and pass the 'data' argument
add_label.AddLabel(data)
