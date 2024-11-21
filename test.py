#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

bool check_combination(const vector<vector<int>>& matrix, const vector<int>& comb, int n) {
    for (int i = 0; i < n; ++i) {
        bool has_zero = false;
        for (int j : comb) {
            if (matrix[i][j] == 0) {
                has_zero = true;
                break;
            }
        }
        if (!has_zero) {
            return false;
        }
    }
    return true;
}

pair<int, vector<int>> find_min_columns(const vector<vector<int>>& matrix, int n, int m) {
    vector<int> columns(m);
    for (int i = 0; i < m; ++i) {
        columns[i] = i;
    }

    for (int k = 1; k <= m; ++k) {
        vector<bool> v(m);
        fill(v.begin(), v.begin() + k, true);
        do {
            vector<int> comb;
            for (int i = 0; i < m; ++i) {
                if (v[i]) {
                    comb.push_back(i);
                }
            }
            if (check_combination(matrix, comb, n)) {
                return {k, comb};
            }
        } while (prev_permutation(v.begin(), v.end()));
    }
    return { -1, {}};
}

int main() {
    ifstream input_file("kill.in");
    ofstream output_file("kill.out");

    int n, m;
    input_file >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            input_file >> matrix[i][j];
        }
    }

    auto result = find_min_columns(matrix, n, m);
    if (result.first == -1) {
        output_file << "Impossible" << endl;
    } else {
        output_file << result.first << endl;
        for (int col : result.second) {
            output_file << (col + 1) << " ";
        }
        output_file << endl;
    }

    input_file.close();
    output_file.close();

    return 0;
}
