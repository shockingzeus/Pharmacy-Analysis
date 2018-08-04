# Pharmacy Counting Program 
 
A Python 3 script that solves the following problem:

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name.

## Requires

Python 3
decimal, Sys and Time (optional) Module

## Input

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name. It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication.

## How it's done

Reading the input is straightforward. We simply read each line as a string, parse it into a list of (5) values and iterate through the lines. 

We use two python dictionaries to organize the data. The keys of the dictionary are the drug names. For each line, we first check if the data make sense, i.e. whether the cost of the medication is a number. We then check if the drug name as a key is already included in the dictionary. If not, add the key to both dictionaries, with the cost of the medication as the value of the first dictionary "AMTdict", and a python set of the patient name as the value of the second dictionary "NAMEdict". If yes, add the cost of the medication to the value of the first dictionary "AMTdict", and check if the name is already included in the python set of names. If no, add the name.

Once we finish building the dictionary, sort the first dictionary by values and keys as a "sorted" object. Iterate over this object to build the output, and write to the output file.


## Usage

run.sh