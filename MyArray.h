//---------------------------------------------------------------
/* MyArray.h*/
#pragma once

class MyArray{
public:
    MyArray(); // Имя консруктора как у создаваемого массива
    MyArray(int siz); //размер
    MyArray(int siz,int v); // размер и элемент

    ~MyArray(); //ДЕСТРУКТОР

    void pushBack(int v); //вставка в конец массива
    void pushFront(int v); //вставка вначало

    void popBack(); //удалить самый послежний эоемент
private:

    int* arr; 
    int size;
    int catapicy;

    void Resize(int offSet);

};
//---------------------------------------------------------------
