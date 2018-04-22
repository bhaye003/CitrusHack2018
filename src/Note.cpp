#include "Note.h"

using namespace std;

Note::Note(string pitch, double length, int velocity){
    this->pitch = pitch;
    this->length = length;
    this->velocity = velocity;
}

string Note::getPitch(){
   cout << this->pitch << endl;
}

double Note::getLength(){
   cout << this->length << endl;
}

int Note::getVelocity(){
   cout << this->velocity << endl;
}
