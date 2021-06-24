#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <climits>

using namespace std;

#define max(a, b) (a > b) ? a : b
#define min(a, b) (a < b) ? a : b

class GameTree {
private:
	map<char, pair<int, vector<char>>> tree;
public:
	GameTree() {
		tree['R'] = make_pair(0, vector<char>(0));
	}
	void add(char parent, vector<char> children) {
		tree[parent].second = children;
	}
	void set_val(char node, int val) {
		tree[node] = make_pair(val, vector<char>(0));
	}
	void print(char parent = 'R') {
		printf("%c: ", parent);
		for(int i = 0; i < tree[parent].second.size(); i++) {
			printf("%c ", tree[parent].second[i]);			
		}
		printf("\n");
		for(int i = 0; i < tree[parent].second.size(); i++) {
			print(tree[parent].second[i]);			
		}		
	}
	int alphabeta(char node = 'R', int alpha = -INT_MAX, int beta = INT_MAX, bool is_maximizer = true) {
		printf("%c\n", node);
		if(tree[node].second.size()) {
			if(is_maximizer) {
				tree[node].first = -INT_MAX;
				for(int i = 0; i < tree[node].second.size(); i++) {
					// printf("%d\n", i);
					int val = tree[node].first;
					int eval = alphabeta(tree[node].second[i], alpha, beta, !is_maximizer);
					tree[node].first = max(val, eval);
					if(tree[node].first >= beta) {
						break;
					}
					alpha = max(alpha, tree[node].first);
				}
			}
			else {
				tree[node].first = INT_MAX;
				for(int i = 0; i < tree[node].second.size(); i++) {
					// printf("%d\n", i);
					int val = tree[node].first;
					int eval = alphabeta(tree[node].second[i], alpha, beta, !is_maximizer);
					tree[node].first = min(val, eval);
					if(tree[node].first <= alpha) {
						break;
					}
					beta = min(beta, tree[node].first);				
				}	
			}
		}
		printf("%c -> %d\n", node, tree[node].first);
		printf("alpha = %d, beta = %d\n", alpha, beta);
		printf("-----\n");
		return tree[node].first;
	}
};

GameTree createTree() {
	GameTree g;
	g.add('R', {'a', 'b', 'c'});
	g.add('a', {'d', 'e', 'f'});
	g.add('b', {'g', 'h'});
	g.add('c', {'i', 'j'});
	g.add('d', {'k', 'l'});
	g.add('e', {'m', 'n'});
	g.add('m', {'o', 'p'});
	g.add('g', {'q', 'r', 's'});
	g.add('q', {'t', 'u'});
	g.add('s', {'v', 'w'});
	g.add('i', {'x', 'y', 'z'});
	g.add('z', {'A', 'B', 'C'});
	g.add('j', {'D', 'E'});
	g.set_val('k', 4);
	g.set_val('l', 13);
	g.set_val('o', 5);
	g.set_val('p', 10);
	g.set_val('n', 11);
	g.set_val('f', 16);
	g.set_val('t', 1);
	g.set_val('u', 8);
	g.set_val('r', 9);
	g.set_val('v', 6);
	g.set_val('w', 12);
	g.set_val('h', 12);
	g.set_val('x', 10);
	g.set_val('y', 8);
	g.set_val('A', 2);
	g.set_val('B', 5);
	g.set_val('C', 7);
	g.set_val('D', 7);
	g.set_val('E', 4);
	return g;
}

int main() {
	GameTree g = createTree();
	// g.print();
	cout << g.alphabeta();
	return 0;
}