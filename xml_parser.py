# -*- coding: utf-8 -*-

from xml.dom import minidom
import time
class menuStatus:
    #inMenu(1) is in, inMenu(0) is out
    def __init__(self, status = 1):
        self.inMenu = status
    def changeStatus(self, status):
        self.inMenu = status
    def getStatus(self):
        return self.inMenu + 0

class Parser:
    def __init__(self):
        self.xmldoc = minidom.parse("Bible.xml")
        
    def parseTestament(self):
        self.Testaments = self.xmldoc.getElementsByTagName("TESTAMENT")
        
    def parseBooks(self, testamentNumber):
        self.testamentNum = testamentNumber
        self.Books = self.Testaments[testamentNumber-1].getElementsByTagName("BIBLEBOOK")
        self.createBookIndex(testamentNumber)
        
    def parseChapters(self, bookNumber):
        self.bookNum = bookNumber
        self.Chapters = self.Books[bookNumber-1].getElementsByTagName("CHAPTER")
        
    def parseVerses(self, chapterNumber):
        if(1 <= chapterNumber and chapterNumber <= len(self.Chapters)):
            self.chapterNum = chapterNumber
            self.Verses = self.Chapters[chapterNumber-1].getElementsByTagName("VERS")
            self.printVerses()
            return 1
        else:
            print "Chapter out of Range"
            return 0
        
    def printVerses(self):
        valid = 0
        while not valid:
            verseIndex = 0
            for Verse in self.Verses:
                print unicode(str(verseIndex+1) + " " + self.Verses[verseIndex].firstChild.nodeValue)
                verseIndex += 1
                
            print ""
            
            option = int(raw_input("OPTIONS: Previous Chapter(0), Next Chapter(1), Exit to Choose Book(2), Exit to Main Menu(3)"))
            
            if(option == 0):
                valid = self.parseVerses(self.chapterNum-1)           
            if(option == 1):
                valid = self.parseVerses(self.chapterNum+1)
                print valid
            if(option == 2):
                self.parseBooks(self.testamentNum)
                BookOptions(self)
                return
            if(option == 3):
                return

    def createBookIndex(self, testamentNumber):
        if testamentNumber == 1 or testamentNumber == 2:
            self.bookNames = self.Books[0:]
            self.printBookIndex(self.bookNames)

            
    def printBookIndex(self, bookNames):
            bookIndex = 1
            #print bookNames
            for bookName in bookNames:
                #print "here"
                print unicode((str(bookIndex) + " " + bookName.getElementsByTagName("CAPTION")[0].firstChild.data))
                bookIndex += 1

    def printBookChapters(self):
        chapterNumber = 1
        tempChapters = self.Chapters[0:]
        #print self.Chapters
        for Chapter in tempChapters:
            print str(chapterNumber) + " ",
            chapterNumber += 1
        print ""                             


def main():
    status = menuStatus()
    count = 0
    #print "hi"
   # print status.inMenu
    start_time = time.time()
    Bible = Parser()
    end_time = time.time()
    print (str(end_time - start_time) + " seconds to parse")
    print "Welcome to Russian Bible"
    while(status.inMenu == 1):
        testamentInput = int(raw_input("Ветхий Завет(1) или Новый Завет(2)? ("+"0"+" to exit)\n"))
        Bible.parseTestament()
        if testamentInput == 0:
            status.changeStatus(0)
        elif testamentInput == 1 or testamentInput == 2:
            Bible.parseBooks(testamentInput)
            BookOptions(Bible)
        else:
            print "Invalid input!"

def BookOptions(Bible):
     bookInput = int(raw_input("Which book would you like to choose?\n"))
     Bible.parseChapters(bookInput)
     ChapterOptions(Bible)
     
def ChapterOptions(Bible):
    valid = 0
    while not valid:
        Bible.printBookChapters()
        chapterInput = int(raw_input("Which chapter would you like to view?\n"))
        valid = Bible.parseVerses(chapterInput)

main()
raw_input("")















    #for Book in Books:
     #   name = Book.getElementsByTagName("CAPTION")[0].firstChild.data
     #   print str(bookindex) + " " + name
     #   bookindex += 1
      #  if Book.getAttribute('bnumber') == "40":
        #     print(name)
         #   Chapters = Book.getElementsByTagName("CHAPTER")
          # for Chapter in Chapters:
           #     if Chapter.getAttribute('cnumber') == "1":
            #        Verses = Chapter.getElementsByTagName("VERS")
             #       index = 0
              #      for Verse in Verses:
               #         #if Verse.getAttribute('vnumber') == "1":
                #            print str(index+1) + " " + Verses[index].firstChild.nodeValue
                 #           index+=1
        #print(name)

