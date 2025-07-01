#include <iostream>
#include "MyArray.h"
#include "MyArray.cpp"

int main(){
    MyArray arr1;
    std::cout<<arr1.getSize()<<" "<<arr1.getCatapicy()<<std::endl;

    MyArray arr2(10);
    std::cout<<arr2.getSize()<<" "<<arr2.getCatapicy()<<std::endl;

    MyArray arr3(5,4);
    std::cout<<arr3.getSize()<<" "<<arr3.getCatapicy()<<std::endl;

    for (int i=0;i<arr3.getSize();i++){
        std::cout<<arr3.getElem(i)<<" ";
    }
    std::cout<<" "<<std::endl;
    arr1.pushBack(10);
    arr1.pushBack(15);
    arr1.pushBack(20);
    for (int i=0;i<arr1.getSize();i++){
        std::cout<<arr1.getElem(i)<<" ";
    }
    std::cout<<" "<<std::endl;
    std::cout<<"Capacity_1 = "<<arr1.getCatapicy()<<std::endl;
    arr1.pushFront(11);
    arr1.pushFront(152);
    arr1.pushFront(20);
    for (int i=0;i<arr1.getSize();i++){
        std::cout<<arr1.getElem(i)<<" ";
    }
    std::cout<<" "<<std::endl;
    std::cout<<"Capacity_2 = "<<arr1.getCatapicy()<<std::endl;
    arr1.popBack();
    arr1.popBack();
    arr1.popBack();
    for (int i=0;i<arr1.getSize();i++){
        std::cout<<arr1.getElem(i)<<" ";
    }
}