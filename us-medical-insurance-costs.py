#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[26]:


#import csv library
import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_status = []
regions = []
insurance_charges = []


# In[27]:


def load_list_data(lst, csv_file, column_name):
    #open csv file
    with open('insurance.csv') as insurance_file:
        #read data from csv file
        insurance_dict = csv.DictReader(insurance_file)
        for row in insurance_dict:
            lst.append(row[column_name])
        return lst


# In[28]:


load_list_data(ages,'insurance.csv','age')
load_list_data(sexes,'insurance.csv','sex')
load_list_data(bmis,'insurance.csv','bmi')
load_list_data(num_children,'insurance.csv','children')
load_list_data(smoker_status,'insurance.csv','smoker')
load_list_data(regions,'insurance.csv','region')
load_list_data(insurance_charges,'insurance.csv','charges')


# In[94]:


class PatientsInfo:
    def __init__(self, patients_age, patients_sex, patients_bmi, patients_children, patients_smoker_status, patients_region, patients_charges):
        self.patients_age = patients_age
        self.patients_sex = patients_sex
        self.patients_bmi = patients_bmi
        self.patients_children = patients_children
        self.patients_smoker_status = patients_smoker_status
        self.patients_region = patients_region
        self.patients_charges = patients_charges
        
    def analyze_ages(self):
        total_age = 0
        for age in self.patients_age:
            total_age += int(age)
        return ("Average Patient Age: " + str(round(total_age/len(self.patients_age), 2)) + " years")
    
    def analyze_sexes(self):
        m = 0
        f = 0
        for sex in self.patients_sex:
            if sex == 'male':
                m += 1
            elif sex == "female":
                f += 1
        return ("There are " + str(f) + " females and " + str(m) + " males.")
    
    def unique_regions(self):
        unique_regions = []
        for region in self.patients_region:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions
    
    def average_charges(self):
        total_charges = 0
        for charge in self.patients_charges:
            total_charges += float(charge)
        return ("Average Patient Charge: " + str(round(total_charges/len(self.patients_charges), 2)))
                
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_age]
        self.patients_dictionary["sex"] = self.patients_sex
        self.patients_dictionary["bmi"] = self.patients_bmi
        self.patients_dictionary["children"] = self.patients_children
        self.patients_dictionary["smoker"] = self.patients_smoker_status
        self.patients_dictionary["regions"] = self.patients_region
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary
    
    def most_regions(self):
        return max(set(self.patients_region), key = self.patients_region.count)


# In[95]:


patients_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_status, regions, insurance_charges)


# In[32]:


patients_info.analyze_ages()


# In[36]:


patients_info.analyze_sexes()


# In[37]:


patients_info.unique_regions()


# In[38]:


patients_info.average_charges()


# In[54]:


patients_info.create_dictionary()


# ## Further Analysis
# For further analysis given in the "Scoping Your Project" hint, I begin with analyzing where the majority of the individuals are from

# In[73]:


patients_info.most_regions()


# This is where I finalized my time working on this project. The remaining analysis I did not attempt were:
# - Figure out what the average age is for someone who has at least one child in this dataset.
# - Look at the different costs between smokers vs. non-smokers.
