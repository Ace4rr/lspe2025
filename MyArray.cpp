//-------------------------------------------------------------------------
/*MyArray.cpp*/
#include <iostream>
#include "MyArray.h"
#include <fstream>
#include <chrono>
/* My array*/

void pushTest(int trials){
    MyArray arr1;
    std::ofstream outfile("c:\\Users\\Student\\Desktop\\MyArray.csv");
    for (int i=0;i<trials;i++){
        std::chrono::_V2::system_clock::time_point sstart = std::chrono::high_resolution_clock::now();
        arr1.pushBack(i); //Затем проверить остальные методы
        auto elapsed = std::chrono::high_resolution_clock::now()-sstart;
        long long milliSec=std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed).count();
        outfile<<milliSec<<std::endl;
    }
}

int main(){
    pushTest(5000);
}

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

int MyArray::getSize(){
    return size;
}
int MyArray::getCatapicy(){
    return catapicy;
}
int MyArray::getElem(int pos){
    return arr[pos];
}


//---------------------------------------------------------------