#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	string readpath;
	string savepath;
	for (int i = 1; i < 1581; ++i)
	{
		readpath = "D:/Mashiro's works/大三上/Software-Requirement/lab3_需求变更/文本处理/文本处理/closed/"+to_string(i) + ".json";
		savepath = "D:/Mashiro's works/大三上/Software-Requirement/lab3_需求变更/文本处理/文本处理/closed_res/" + to_string(i) + ".txt";
		//cout << readpath;
		ifstream rd(readpath);
		ofstream wt(savepath, ios::_Noreplace);
		string temp;
		string res;
		bool judge = true;
		if (!rd.is_open())
		{
			cout << "未成功打开文件" << endl;
		}
		while (getline(rd, temp))
		{
			int t = temp.find('"')+1;
			if (t != 0)
			{
				int m = temp.find("\",");
				int n = t;
				if (m == -1)
				{
					m = temp.size();
					judge = false;
				}
				else if (judge == false)
				{
					n = 0;
					judge = true;
				}
				while (t < m)
				{
					//cout << temp[t];
					if (temp[t] == '\\'&&temp[t + 1] == 'n')
					{
						temp.erase(t,2);
						temp.insert(t," ");
						t = t - 1;
						m = m - 2;
					}
					if (temp[t] == '\\'&&temp[t + 1] == '"')
					{
						temp.erase(t, 2);
						temp.insert(t, " ");
						t = t - 1;
						m = m - 2;
					}
					t = t + 1;
				}
				res.assign(temp, n, m - n);
				//cout << res << endl;
				wt << res << endl;
			}
		}
		wt.close();
		cout << i << endl;
	}
	return 0;
}