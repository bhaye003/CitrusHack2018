#ifndef _MFILE_H_
#define _MFILE_H_
#include<iostream>
#include<string>
#include<vector>

#include "Note.h"

class MFile{
    private:
        int tempo;
        double time_sig;
        vector<Note> NoteVec;
    
    public:
        MFile(int tempo, double time_sig);
        void addNote(Note(string pitch, double length, int velocity));
};

#endif
