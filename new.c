#include <stdio.h>

struct point {
   int x;
   int y;
};
struct point my_point = { 3, 7 };
struct point *p = &my_point;

// give address of my_point to a pointer
// in order to access and change the varaible we can use (*p).y or my_point.y or p->y
// (*p).y is the same as p->y


int main(){

    (*p).y = 98;
    printf("%d", my_point);
    my_point.y = 98;
    printf("%d", my_point);
    (*p).y = 98;
    p->y = 98;
}
