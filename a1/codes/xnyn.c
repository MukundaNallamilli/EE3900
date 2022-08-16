#include <stdio.h>

#define N 20

int x(int n){
    if(n < 0){return 0;}
    if(n > 5){return 0;}
    switch (n){
        case 0: return 1;
        case 1: return 2;
        case 2: return 3;
        case 3: return 4;
        case 4: return 2;
        case 5: return 1;
    }
    return 0;
}

float y(int n){
    if(n < 0){return 0;}
    return x(n) + x(n-2) - ((float)(y(n-1)))/2;
}

int main(){
    FILE *fp;
    fp = fopen("3_3_x.dat", "w");
    for(int i = 0; i < 6; i++){
        fprintf(fp, "%d\n", x(i));
    }
    fclose(fp);

    fp = fopen("3_3_y.dat", "w");
    for(int i = 0; i < N; i++){
        fprintf(fp, "%f\n", y(i));
    }
    fclose(fp);
    return 0;
}
