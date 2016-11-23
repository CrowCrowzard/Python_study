#!/usr/bin/env python3
# coding: UTF-8

def get_n_gram(target, n):
    n_gram = []
    for i in range(len(target)-n+1):
        n_gram.append(target[i:i+n])
    return n_gram

def get_union(x, y):
    union = []
    union.append(x)
    for w in y:
        if w not in x:
            union.append(w)
    return union

def get_intersection(x, y):
    intersection = []
    for w in x:
        if w in y:
            intersection.append(w)
    return intersection

def get_difference(x, y):
    difference = []
    for w in x:
        if w not in y:
            difference.append(w)
    return difference

def main():
    X = get_n_gram('paraparaparadise', 2)
    Y = get_n_gram('paragraph' , 2)

    print ('和集合', end='')
    print (get_union(X,Y))
    
    print ('積集合', end='')
    print (get_intersection(X,Y))

    print ('差集合', end='')
    print (get_difference(X,Y))

    
    print ('"se" が Xに含まれるか', end='')
    print ('se' in X)
    
    print ('"se" が に含まれるか', end='')
    print ('se' in Y)

if __name__ == '__main__':
    main()

