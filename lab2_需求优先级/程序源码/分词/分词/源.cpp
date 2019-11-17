#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream rd("data1.txt");
	//ofstream wt1("data2.txt", ios::_Noreplace);
	//ofstream wt2("data3.txt", ios::_Noreplace);
	//ofstream wt3("data4.txt", ios::_Noreplace);
	//ofstream wt4("traindata.txt", ios::_Noreplace);
	FILE*fp = fopen("traindata2.txt", "w");
	string temp;
	bool judge = true;
	if (!rd.is_open())
	{
		cout << "未成功打开文件" << endl;
	}
	int count = 0;
	while (getline(rd, temp))
	{
		int i = 0;
		int ter1 = temp.find(' ');
		int ter2 = temp.find(' ',ter1 + 1);
		while (temp[i] != '\0')
		{
			if ((temp[i] >= 'a'&&temp[i] <= 'z') || (temp[i] >= '0'&&temp[i] <= '9') || (temp[i] >= 'A'&&temp[i] <= 'Z')||temp[i]==' ')
			{
				//cout << temp[i];
				if (i > ter2)
					fprintf(fp, "%c", temp[i]);
			}
			++i;
		}
		fprintf(fp, "%c", '\n');
		//cout << temp;
		//cout << endl;
		//int i = 0;
		////cout << "k" << endl;
		//temp = "[\'" + temp;
		//int t = temp.find(' ');
		//string temp2 = temp.substr(t + 1);
		//int tempt = temp2.find(' ');
		//string temp3 = temp2.substr(tempt + 1);
		//while (t != temp.npos)
		//{
		//	/*cout << temp << endl;
		//	cout << t << endl;*/
		//	temp.replace(t, 1, "\',\'");
		//	t = temp.find(' ');
		//}
		//temp = temp + "\'],";
		//temp2 = "[\'" + temp2;
		//t = temp2.find(' ');
		//while (t != temp2.npos)
		//{
		//	temp2.replace(t, 1, "\',\'");
		//	t = temp2.find(' ');
		//}
		//temp2 = temp2 + "\'],";
		//temp3 = "[\'" + temp3;
		//t = temp3.find(' ');
		//while (t != temp3.npos)
		//{
		//	temp3.replace(t, 1, "\',\'");
		//	t = temp3.find(' ');
		//}
		//temp3 = temp3 + "\'],";
		////cout << temp << endl;
		//wt1 << temp << endl;
		//wt2 << temp2 << endl;
		//wt3 << temp3 << endl;
	}
	fclose(fp);
	return 0;
}