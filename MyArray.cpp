//-------------------------------------------------------------------------
/* Day2_1.cpp*/
#include <iostream>
#include "MyArray.h"
/* My array*/

MyArray::MyArray(){
    size=0;
    catapicy=5;

    arr=new int[catapicy];

}

MyArray::MyArray(int siz){
    size=siz;
    catapicy=siz+1;

    arr=new int[catapicy];
}

MyArray::MyArray(int siz,int v){
    size=siz;
    catapicy=siz+1;

    arr=new int[catapicy];

    for (int i=0;i<size;++i){
        arr[i]=v;

    }
}

MyArray::~MyArray(){ //ДЕСТРУКТОР
    delete [] arr; //Означает что надо удалить все ячейки

}

void MyArray::Resize(int offSet){
    int* oldArr=arr;
    int* newArr=new int[catapicy*2];
    
    for (int i=0;i<size;i++){
        newArr[i]=oldArr[i];
    
    }

    delete[] oldArr;
    arr=newArr;
    catapicy*=2;
}

void MyArray::pushBack(int v){
    
    if (size==catapicy){
        Resize(v);
    }
    size++;
    arr[size-1]=v;
}

void MyArray::pushFront(int v){
    if (size==catapicy){
        Resize(v);
    }
    for (int i=size-1;i>=0;i--){
        arr[i+1]=arr[i];
    }
    ++size;
    arr[0]=v;
}

void MyArray::popBack(){
    if (size==0){
        return;
    }
    
    --size;
}

//---------------------------------------------------------------
