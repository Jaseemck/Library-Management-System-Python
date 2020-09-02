import stock

def main():
    while(True):
        print(">>>>>>>>Library Management Software<<<<<<<<<")
        print("-----------------------------------------------------------------------------")
        print("OPTIONS:")
        print("(1)Add Books (2)Search Books (3)Issue Books (4)Return Books (5)List (6)Exit")
        try:
            a=int(input("Select an Option from Above: "))
            if(a==1):
                with open("stock.txt", "a") as stock_file:
                    name=input("Enter the books Name: ")
                    author=input("Enter the Author Name: ")
                    stock_file.write(name+","+author+","+"False\n")
            elif(a==2):
                search = input("Enter Name of the book to search: ")
                stock.stock()
                flag=False
                i=0
                for book in stock.bookName:
                    if book==search:
                        name=stock.bookName[i]
                        author=stock.authorName[i]
                        issue=stock.issued[i]
                        print("Book is Available")
                        flag=True
                        break
                    i=i+1
                if flag==True:
                    print("Name: "+name+"   Author:"+author+"    Status:"+issue)
                else:
                    print("The book is not available!")
            elif(a==3):
                borrow = input("Enter the name of the book to borrow: ")
                stock.stock()
                flag=False
                i=0
                for book in stock.bookName:
                    if book==borrow and stock.issued[i]=="False":
                        name=stock.bookName[i]
                        author=stock.authorName[i]
                        print("Book is Available! ThankYou for buying")
                        flag=True
                        break
                    i=i+1
                index=i
                if(flag==True):
                    with open("stock.txt",'r') as f:
                        get_all=f.readlines()
                    with open("stock.txt",'w') as f:
                        for i,line in enumerate(get_all):
                            if i == index:
                                f.writelines(name+","+author+","+"True\n")
                            else:
                                f.writelines(line)
                else:
                    print("Sorry! The book is not available")
            elif(a==4):
                return_book = input("Enter the name of the book to return: ")
                stock.stock()
                flag=False
                i=0
                for book in stock.bookName:
                    if book==return_book and stock.issued[i]=="True":
                        name=stock.bookName[i]
                        author=stock.authorName[i]
                        print("ThankYou for returning the book")
                        flag=True
                        break
                    i=i+1
                index=i
                if(flag==True):
                    with open("stock.txt",'r') as f:
                        get_all=f.readlines()
                    with open("stock.txt",'w') as f:
                        for i,line in enumerate(get_all):
                            if i == index:
                                f.writelines(name+","+author+","+"False\n")
                            else:
                                f.writelines(line)
                else:
                    print("Please check the name of the book!")
            elif(a==5):
                stock.stock()
                print("| Book Name | Author | Issued |")
                for i in range(len(stock.bookName)):
                    print("| "+stock.bookName[i]+" | "+stock.authorName[i]+" | "+stock.issued[i]+" |")
            elif(a==6):
                print("Thank You for using the Software!")
                break
            else:
                print("Enter a valid input!")
        except:
            print("Value Error")

main()
