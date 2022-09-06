#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;
using std::setw;

class node
{
public:
    string name;
    int score;
    node *prev;
    node *next;
    node(string _name, int _score, node *prevp = NULL, node *nextp = NULL)
    {
        name = _name;
        score = _score;
        prev = prevp;
        next = nextp;
    }
    node(node *prevp = NULL, node *nextp = NULL)
    {
        prev = prevp;
        next = nextp;
    }
};

class score
{
public:
    node *head;
    node *fence;
    node *tail;
    node *temp;
    int cnt;
    void init()
    {
        fence = tail = head = new node();
        cnt = 0;
    }
    void removeall()
    {
        while (head != NULL)
        {
            fence = head;
            head = head->next;
            delete fence;
        }
    }
    score()
    {
        init();
    }
    ~score()
    {
        removeall();
    }
    void clear()
    {
        removeall();
        init();
    }
    void sort(node *nn)
    {
        fence = head;
        while (fence != NULL)
        {
            if (fence->score < nn->score)
            {
                fence = fence->prev;
                nn->next = fence->next;
                nn->prev = fence;
                fence->next->prev = nn;
                fence->next = nn;
                break;
            }
            else
            {
                if (fence->next == NULL)
                {
                    tail->next = nn;
                    nn->prev = fence;
                    tail = nn;
                    tail->next = NULL;
                    break;
                }
            }
            fence = fence->next;
        }
    }
    void insert(string _name, int _score)
    {
        node *nn = new node(_name, _score);
        cnt++;
        if (cnt > 10)
        {
            if (_score > tail->score)
            {
                cout << tail->name << " was remove from the scoreboard !" << endl;
                    temp = tail;
                tail = tail->prev;
                tail->next = NULL;
                delete temp;
                sort(nn);
            }
            else
            {
                cout << "You are not allow to this scoreboard!"
                    << endl;
            }
        }
        else if (head == NULL)
        {
            head = nn;
            tail = nn;
        }
        else
        {
            sort(nn);
        }
    }
    int display()
    {
        fence = head->next;
        while (fence != NULL)
        {
            cout << setw(10) << fence->name;
            cout << setw(15) << fence->score << " " << endl;
            fence = fence->next;
        }
    }
};

int main()
{
    score sc;
    string name;
    int i, score;
    cout << "================================" << endl;
    cout << " Scoreboard " << endl;
    cout << "================================" << endl;
    cout << setw(10) << "Name" << setw(15) << "Score" << endl;
    sc.insert("Book", 60);
    sc.insert("Piam", 80);
    sc.insert("Pee", 55);
    sc.insert("Art", 22);
    sc.insert("Beam", 18);
    sc.insert("Mask", 100);
    sc.insert("Aom", 34);
    sc.insert("Eye", 9);
    sc.insert("Jo", 71);
    sc.insert("Jame", 30);
    sc.display();
    cout << "================================" << endl;
    while (true)
    {
        cout << "Player Name : ";
        cin >> name;
        cout << "Player Score : ";
        cin >> score;
        sc.insert(name, score);
        cout << "================================" << endl;
        cout << " Scoreboard " << endl;
        cout << "================================" << endl;
        cout << setw(10) << "Name" << setw(15) << "Score" << endl;
        sc.display();
        cout << "================================" << endl;
    }
}
