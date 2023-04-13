### \\\\\\\\\\\     Importing The Json Module  ////////// ###
import json

### \\\\\\\\\\     IMPORT MAIN FILE    ///////// ###
 
from Books_Lib import Books_Lib


while True:
    
###  \\\\\\\\\\\    OPENING THE JSON FILE AS THE READING MODE IT WILL ALWAYS EXICUTE    //////////// ###
    
    with open("DataOFbooks.json") as ReadJSONFile:
        try:
            JSONDataBooks = json.load(ReadJSONFile)
                    
        except json.decoder.JSONDecodeError as e:
            print("JSONDecodeError:",e,"\nPlease Add Few Books First Before Reading..")

###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION    //////////// ###

    choice=int(input("\nEnter the Choice \n\n1. Add_Books \t\t2. Show_Books_list \n\n3. Update_Data \t\t4. Delete_Books \n\n5. Author_Names \t6. Existing..\n\t\n :-"))

###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION OF ADDING THE BOOKS     //////////// ###
    try:
        if choice == 1:
            print("Adding The Books Records")
            Book_Id=int(input("Enter The Book_ID : "))
            Book_Name=input("Enter The Book_Name : ")
            Book_Author=input("Enter The Book_Author Name : ")
            Book_Published=int(input("Enter The Date of Book Published : "))
            Book_Price=int(input("Enter The Book_Price : "))
            
           
            ### \\\\\\\\\\\\  PASSING THE THE DATA TO BOOK   ////////////   ###
            
            books_obj = Books_Lib(Book_Id,Book_Name,Book_Author,Book_Published,Book_Price)
            Books_JSONStructre = books_obj.getJSONFormatBook()
            

            ### //////////// CREATE A MAIN KEY /////////////  ###
            JSONDataBooks[Book_Id]=Books_JSONStructre
            

            ### /////////////  DATA IS ADDED TO THE JSON FILE SUCESSFULLY  //////////// ###
            with open('DataOFbooks.json','w') as JSONFile:
                json.dump(JSONDataBooks,JSONFile)
            print("Book Record Added Sucessefully...!")
            
    ###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION OF  SHOW THE DATA     //////////// ###

        elif choice == 2:
            print("Showing The List of ALL BOOKS ")
             

            count = 0
            for Book_Id,book in JSONDataBooks.items():
                    print(Book_Id,book)

                    count = count+1
                    
                    if count%10==0:
                        ch1 = input("\n\tDo you want to see next book (Y/N):-")
                        if ch1=='Y' or ch1=='y':
                            continue
                        else:
                            break
                            
            


    ###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION OF  UPDATE THE GIVEN DATA    //////////// ###

        elif choice == 3:
            print("\nUpdateing The Books Data ")
            
            
            Book_Id = input("Enter Book ID to  update:")
            book_Price =int(input("Enter The Book Updated Price:"))
            
            JSONDataBooks[Book_Id]["book_Price"] = book_Price
            
            
            with open('DataOFbooks.json','w') as JSONFile:
                json.dump(JSONDataBooks,JSONFile)
            print("Book Record Updated!")

            
    ###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION  OF DELETE DATA FROM JSON FILE  //////////// ###

        elif choice == 4:
            print("\nDeleting The Books Data")
             
            
            Book_Id = input("Enter Book ID to delete:")
            JSONDataBooks.pop(Book_Id)
            
            with open('DataOFbooks.json','w') as JSONFile:
                json.dump(JSONDataBooks,JSONFile)
                
            print("Book Record Deleted Sucessefully ")

    ###  \\\\\\\\\\\    CHOICE GIVEN TO PERFORM THE OPERATION OF SHOWING THE NAME OF AUTHOR     //////////// ###


        elif choice == 5:
            print("\nShowing The List of Books Author ")
                    
            for book in JSONDataBooks.values():
                    print(book['auth_name'])
                    
            print("Showed all authors!")

    ###  \\\\\\\\\\\    CHOICE GIVEN TO EXIST FROM PROGRAME     //////////// ###


        elif choice == 6:
            print("Existing The Programe... ")
            break

        else:
            print("Invalid Choice BY You Please Give Valid Response")    
                         
    except:
        print("Invalid Choice BY You Please Give Valid Response")


    
else:
    print("Thanks For Visiting...!!!!")
