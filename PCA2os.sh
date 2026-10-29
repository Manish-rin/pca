#!/bin/bash
# Function to find GCD of two numbers using Euclidean algorithm
gcd() {
    local a=$1
    local b=$2
    while [ $b -ne 0 ]; do
        local temp=$b
        b=$((a % b))
        a=$temp
    done
    echo $a
}

echo "Enter three positive integers separated by space:"
read n1 n2 n3

# Find GCD of first two, then GCD with the third
g1=$(gcd $n1 $n2)
g_final=$(gcd $g1 $n3)

# Find LCM of three numbers using formula: LCM(a,b,c) = LCM(LCM(a,b), c)
# LCM(x, y) = (x * y) / GCD(x, y)
l1=$(( (n1 * n2) / g1 ))
l_12=$(gcd $l1 $n3)
l_final=$(( (l1 * n3) / l_12 ))

echo "GCD of $n1, $n2, $n3 is: $g_final"
echo "LCM of $n1, $n2, $n3 is: $l_final"

# q2
#!/bin/bash

echo "Enter a number:"
read num

n=$num
sum=0
# Find total digits dynamically
num_digits=${#num}

while [ $n -gt 0 ]; do
    digit=$((n % 10))
    # Calculate digit raised to power of num_digits
    power=$((digit ** num_digits))
    sum=$((sum + power))
    n=$((n / 10))
done

if [ $sum -eq $num ]; then
    echo "$num is an Armstrong number."
else
    echo "$num is NOT an Armstrong number."
fi

# q3
#!/bin/bash

echo "Enter lower limit (m):"
read m
echo "Enter upper limit (n):"
read n

sum=0
echo "Prime numbers between $m and $n are:"

for ((i=m; i<=n; i++)); do
    if [ $i -lt 2 ]; then
        continue
    fi
    is_prime=1
    for ((j=2; j*j<=i; j++)); do
        if [ $((i % j)) -eq 0 ]; then
            is_prime=0
            break
        fi
    done
    if [ $is_prime -eq 1 ]; then
        echo -n "$i "
        sum=$((sum + i))
    fi
done

echo ""
echo "Sum of all prime numbers between $m and $n is: $sum"

# q4
#!/bin/bash

echo "Enter 5 numbers separated by space:"
read a b c d e

# Initialize largest and second largest
largest=$a
second=-999999

for num in $b $c $d $e; do
    if [ $num -gt $largest ]; then
        second=$largest
        largest=$num
    elif [ $num -gt $second ] && [ $num -ne $largest ]; then
        second=$num
    fi
done

echo "The second-largest number is: $second"

# Question 2: Q2. One-Dimensional Array Programming (Any two – 10 Marks)
# 1
#!/bin/bash

echo "Enter elements of the array separated by space:"
read -a arr

echo "Displaying elements with their indices:"
for i in "${!arr[@]}"; do
    echo "Index $i: ${arr[$i]}"
done

# 2
#!/bin/bash

echo "Enter elements of the array separated by space:"
read -a arr

smallest=${arr[0]}
largest=${arr[0]}
second_largest=-999999

for val in "${arr[@]}"; do
    if [ $val -lt $smallest ]; then
        smallest=$val
    fi
    if [ $val -gt $largest ]; then
        second_largest=$largest
        largest=$val
    elif [ $val -gt $second_largest ] && [ $val -ne $largest ]; then
        second_largest=$val
    fi
done

echo "Smallest element: $smallest"
echo "Second-largest element: $second_largest"


# 3
#!/bin/bash

echo "Enter elements of the array separated by space:"
read -a arr

echo "Enter the element to search:"
read target

count=0
for val in "${arr[@]}"; do
    if [ "$val" -eq "$target" ]; then
        count=$((count + 1))
    fi
done

echo "Element $target found $count time(s) in the array."

# Q3. On Command (5 Marks)
Here are the standard Linux terminal commands to answer each sub-bullet:

    /*Display disk usage of all mounted file systems:
    Bash

    df -h

    Display file-system types along with disk usage:
    Bash

    df -hT

    Display disk usage of the root (/) file system:
    Bash

    df -h /

    Identify the file system with the highest disk usage:
    Bash

    df -h | sort -k 5 -hr | head -n 2

    Display the available and used disk space of all mounted file systems:
    Bash

    df -BM
    # Or standard human-readable format showing used and available columns:
    df -h
*/