#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream rd("issue.json");
	ofstream wt1("data1.txt", ios::_Noreplace);
	ofstream wt2("data2.txt", ios::_Noreplace);
	ofstream wt3("data3.txt", ios::_Noreplace);
	ofstream wt4("data4.txt", ios::_Noreplace);
	ofstream wt5("data5.txt", ios::_Noreplace);
	string temp;
	bool judge = true;
	if (!rd.is_open())
	{
		cout << "未成功打开文件" << endl;
	}
	int i = 0;
	int count = 0;
	while (getline(rd, temp))
	{
		//cout << "k" << endl;
		if (temp=="    [")
		{
			getline(rd, temp);
			cout << temp<<endl<<i<<" "<<count << endl;
			if (i == 0)
			{
				wt1 << temp << endl;
			}
			else if (i == 1)
			{
				wt2 << temp << endl;
			}
			else if (i == 2)
			{
				wt3 << temp << endl;
			}
			else if (i == 3)
			{
				wt4 << temp << endl;
			}
			else
			{
				wt5 << temp << endl;
			}
			//cout << 't' << endl;
			++count;
			if (count == 999)
			{
				count = 0;
				++i;
			}
		}
	}
	cout << i;
	return 0;
}