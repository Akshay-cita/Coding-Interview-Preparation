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

