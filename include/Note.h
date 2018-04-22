#ifndef __NOTE_H__
#define __NOTE_H__
#include <iostream>
#include <string>

class Note {
    public:
        Note(string pitch, double length, int velocity);
        getPitch();
        getLength();
        getVelocity();
        
    private:
        string pitch;
        double length;
        int velocity;
};

#endif