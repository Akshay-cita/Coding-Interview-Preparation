# Coding-Interview-Preparation
Coding Interview Preparation
## Day-1: Sales by match
* [HackerRank Problem](https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)
## Day-2: Base25 to Base10 conversion
Consider a base 26 system wherein the letters of the alphabets are the digits.

That is A=0, B=1, C=2….Z=25 in base 10

Write a program that will take an input string of alphabets, use the first half of the string as a number in the base26 system and the other half as another number in the base26 system.Now, add these two numbers to obtain a sum in base10.
Accept the string only if it contains even number of characters otherwise, return 0.

Example:-  If your input string is “Petpan”, then first split it into PET26 and PAN26. And show the sum in base10.

#### Sample Input

“Petpan”

#### Sample Output
20416

## Day-3 : Mean, Median, and Mode

Calculating the mean, median, and mode

#### Mean:

We sum all elements in the array, divide the sum by
if the array {X1,X2,X3,...,Xn},Finding Mean of the array is (X1+X2+X3+...+Xn)/n

Here ' n ' is number of elements in the array,
#### Median:

To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order.
We then average the two middle elements

* If the array is odd number of length the Median will be exactly the middle element of an array

Ex: Consider an array of length 3(The length of array is odd number){X1,X2,X3},the median is X2(i.e,exactly middle element of the array)

* If the array is even number of length the Median will be sum of middle elements and devide the sum by 2

Ex: Consider an array of length 4(The length of array is even number){X1,X2,X3,X4},the median is (X2+X3)/2

#### Mode:

We can find the number of occurrences of all the elements in the array.The maximum no.of occurence element will be the mode of the array

Ex:Consider an array of length 7, {X1,X2,X2,X4,X3,X4,X4}, The mode is X4 .i,e. X4 is repeating 4 time.So the mode of the array is X4

Assignment: Find who tweeted the most

## Day-4 : User with max number of Tweets

Given a list of tweets
Program should find the user who has tweeted the most


Input format:
1. Read the input from console.
2. First line of input should be number of test cases
3. Remaining lines of input should contain each test case input. 


For each test case input:
1. First line should contain number of tweets.
2. Followed by N lines, each containing user name and tweet id separated by a space.

Output format:
Find the user with max number of tweets. Print user name and total number of tweets.

If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.


Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4


Output
sachin 3




Sample 2:
Input 
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6


Output
kohli 2
sachin 2
sehwag 2






Sample 3:
Input 
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14


Output
sachin 2
Sehwag 2
dhoni 4


## Day-5 : Bitwise AND

You are given n positions and each position has a value associated with it.You can delete only two positions but their Bitwise AND should be greater than k,Dettermine the numbers of pairs of positions whose Bitwise AND value is greater than k.

Sample:

3 (Value of n)

1 2 3 (Values)

0 (value of k)

Output:

The pairs are: ('1', '3')

The pairs are: ('2', '3')

2

Explaination: There are 3 positions and associated values are 1 2 3. The pairs whose Bitwise value greater than k is 1 and 3 or 2 and 3. So there are 2 pairs.Out put is 2. 



