# Frequent-Pattern-Mining
Data Mining- Implementation of Frequent Pattern Mining Algorithm

This code is being done as the assignment of CS 412- Intro to Data Mining (Spring 2018), University of Illinois at Urbana Champaign.

Rules for Implementation are mentioned below.

Input Format

The input dataset is a transaction dataset.

The first line of the input corresponds to the minimum support.

Each following line of the input corresponds to one transaction. Items in each transaction are seperated by a space.

Please refer to the sample input below. In sample input 0, the minimum support is 2, and the dataset contains 3 transactions and 5 item types (A, B, C, D and E).

Constraints

NA

Output Format

The output are the frequent patterns you mined out from the input dataset.

Each line in the output should be of the format :

Support [frequent pattern]

Frequent patterns should be listed in a descending order based on support. e.g. 3 [C] is listed before 2 [A].
Ties should be resolved based on lexicographical order. e.g. 2 [A] is listed before 2 [A C]
Items within each pattern should be listed in lexicographical order as well seperated by a single space. e.g. 2 [B C D]
First print the frequent patterns and then closed pattern. Seperate the output for two parts by an empty line. In sample output 0, first 9 lines correspond to frequent patterns and last 3 lines correspond to closed pattern.
