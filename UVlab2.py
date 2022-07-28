"""
UV absorption spectra of conjugated systems
by Shane Gervais
This class is used to find the peaks of our
dye spectra's from our physical chemistry lab.
We will also be conducting beers law for 
molar extinction coefficients.
"""

#Import methods that will help us for the analysis
import pandas as pd
import io
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np

dye1 = pd.read_excel('Export Data Dy1UV2_NS.xlsx')
dye2 = pd.read_excel('Export Data Dy2_UV2_NS.xlsx')
dye3 = pd.read_excel('Export Data Dy3_UV3_NS.xlsx')


absorption1 = dye1.Abs
wavelength1 = dye1.Wavelength
absorption1 = np.array(absorption1)
wavelength1 = np.array(wavelength1)

absorption2 = dye2.Abs
wavelength2 = dye2.Wavelength
absorption2 = np.array(absorption2)
wavelength2 = np.array(wavelength2)

absorption3 = dye3.Abs
wavelength3 = dye3.Wavelength
absorption3 = np.array(absorption3)
wavelength3 = np.array(wavelength3)


#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelength1,absorption1,'r-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()

#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelength2,absorption2,'b-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()

#Plots our data from the excel sheet
plt.figure(figsize = (10, 5))
plt.plot(wavelength3,absorption3,'g-o')
plt.ylabel("Absorptions")
plt.xlabel("Wavelength (/nm)")
plt.show()

peak1 = []
for i in range(0, len(absorption1)):
    if absorption1[i] == max(absorption1):
        peak1.append(i)


peakWave1 = wavelength1[peak1[0]]
print("The peak Wavelength for dye1 is at ", peakWave1, " nm", " at the absorption ", max(absorption1))


peak2 = []
for i in range(0, len(absorption2)):
    if absorption2[i] == max(absorption2):
        peak2.append(i)


peakWave2 = wavelength2[peak2[0]]
print("The peak Wavelength for dye2 is at ", peakWave2, " nm", " at the absorption ", max(absorption2))


peak3 = []
for i in range(0, len(absorption3)):
    if absorption3[i] == max(absorption3):
        peak3.append(i)


peakWave3 = wavelength3[peak3[0]]
print("The peak Wavelength for dye3 is at ", peakWave3, " nm", " at the absorption ", max(absorption3))



l = 1 #cm
concentrations = [0.12222295587102454, 0.02635599853450573, 0.013337743375064177]
print("The concentration of dye1 is: ", concentrations[0], " mol/L")
print("The concentration of dye2 is: ", concentrations[1], " mol/L")
print("The concentration of dye3 is: ", concentrations[2], " mol/L")

#Dye1
epsi1 = (max(absorption1))/(concentrations[0]*l)
print("The molar extinction coefficient for Dye1 is: ", epsi1, " L/mol*cm")

#Dye2
epsi2 = (max(absorption2))/(concentrations[1]*l)
print("The molar extinction coefficient for Dye2 is: ", epsi2, " L/mol*cm")

#Dye3
epsi3 = (max(absorption3))/(concentrations[2]*l)
print("The molar extinction coefficient for Dye3 is: ", epsi3, " L/mol*cm")