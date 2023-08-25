#include <bits/stdc++.h>
using namespace std;
int main()
{
    //auto-generate a script1 which will send 1 lakh inputs to the ssh server
    std::ofstream script1;
    script1.open("script1.sh");
    //log file stores output of the game screen
    script1 << "log_file -a game_outputs.log\n";
    script1 << "spawn ssh student@172.27.26.188\n";
    string sshpwd, gpname, gppwd, infile;
    cout << "Enter your SSH Password : ";
    cin >> sshpwd;
    cout << "\nEnter your team name : ";
    cin >> gpname;
    cout << "\nEnter your team pwd : ";
    cin >> gppwd;
    script1 << "expect  \"student@172.27.26.188's password:\"\n";
    script1 << "send -- \"";
    script1 << sshpwd;
    script1 << "\\r\"\n\n";
    script1 << "expect  \"group name:\"\n";
    script1 << "send -- \"";
    script1 << gpname;
    script1 << "\\r\"\n\n";
    script1 << "expect  \"password:\"\n";
    script1 << "send -- \"";
    script1 << gppwd;
    script1 << "\\r\"\n\n";
    script1 << "expect  \"at:\"\n";
    script1 << "send -- \"4\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"back\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"enter\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"wave\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"back\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"back\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"thrnxxtzy\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"read\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"the_magic_of_wand\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"c\\r\"\n\n";
    script1 << "expect  \"> \"\n";
    script1 << "send -- \"read\\r\"\n\n";
    std::ifstream input_random1("plaintext1.txt");
    std::string line1;
    if (input_random1.is_open())
    {
        while (std::getline(input_random1, line1))
        {
            script1 << "expect  \"> \"\n";
            script1 << "send -- \"";
            script1 << line1;
            script1 << "\\r\"\n\n";
            script1 << "expect  \"> \"\n";
            script1 << "send -- \"c\\r\"\n\n";
        }
        input_random1.close();
    }
    script1.close();

    std::ofstream script2;
    script2.open("script2.sh");
    //log file stores output of the game screen
    script2<< "log_file -a game_outputs.log\n";
    script2<< "spawn ssh student@172.27.26.188\n";
    cout << "Enter your SSH Password : ";
    cin >> sshpwd;
    cout << "\nEnter your team name : ";
    cin >> gpname;
    cout << "\nEnter your team pwd : ";
    cin >> gppwd;
    script2<< "expect  \"student@172.27.26.188's password:\"\n";
    script2<< "send -- \"";
    script2<< sshpwd;
    script2<< "\\r\"\n\n";
    script2<< "expect  \"group name:\"\n";
    script2<< "send -- \"";
    script2<< gpname;
    script2<< "\\r\"\n\n";
    script2<< "expect  \"password:\"\n";
    script2<< "send -- \"";
    script2<< gppwd;
    script2<< "\\r\"\n\n";
    script2<< "expect  \"at:\"\n";
    script2<< "send -- \"4\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"back\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"enter\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"wave\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"back\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"back\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"thrnxxtzy\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"read\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"the_magic_of_wand\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"c\\r\"\n\n";
    script2<< "expect  \"> \"\n";
    script2<< "send -- \"read\\r\"\n\n";
    std::ifstream input_random2("plaintext2.txt");
    std::string line2;
    if (input_random2.is_open())
    {
        while (std::getline(input_random2, line2))
        {
            script2<< "expect  \"> \"\n";
            script2<< "send -- \"";
            script2<< line2;
            script2<< "\\r\"\n\n";
            script2<< "expect  \"> \"\n";
            script2<< "send -- \"c\\r\"\n\n";
        }
        input_random2.close();
    }
    script2.close();


}