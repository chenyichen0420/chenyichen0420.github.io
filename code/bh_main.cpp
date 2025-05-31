#include<bits/stdc++.h>
#include<locale>
using namespace std;
ifstream in;
ofstream out;
int cnt;
string n;
vector<string>url;
vector<string>nam;
string cookie;
int ty;
int main() {
	locale::global(locale("zh_CN.UTF-8"));
	in.open("hackset.txt");
	out.open("bilhak.txt");
	getline(in, cookie);
	out << cookie << endl;
	in >> cnt >> ty; out << cnt << endl;
	for (int i = 1; i <= cnt; ++i)
		in >> n, url.push_back(n),
		in >> n, nam.push_back(n),
		out << url.back() << endl;
	in.close(); out.close();
	system("bilihacker.exe < bilhak.txt");
	for (int i = 0; i < cnt; ++i) {
		string audio = "video\\" + url[i] + ".mp3";
		string video = "video\\" + url[i] + ".mp4";
		string outio = nam[i] + ".mp4";
		string aunio = nam[i] + "-aud.mp3";
		string vineo = nam[i] + "-vid.mp4";
		string cmd;
		if (ty & 4)
			cmd =
			(string)R"(ffmpeg.exe)" +
			" -i " + video +
			" -i " + audio +
			" -vcodec copy -acodec copy " +
			outio,
			system(cmd.c_str());
		if (ty & 1)
			cmd =
			"move " +
			audio + " " +
			aunio,
			system(cmd.c_str());
		else
			cmd =
			"del /f " +
			audio,
			system(cmd.c_str());
		if (ty & 2)
			cmd =
			"move " +
			video + " " +
			vineo,
			system(cmd.c_str());
		else
			cmd =
			"del /f " +
			video,
			system(cmd.c_str());
	}
	system("pause");
}
