class Solution {
public:
    int myAtoi(std::string s) {
        int index = 0;
        while (index < s.size() && s[index] == ' ') {
            index++;
        }
        int sign = 1;
        if (index < s.size() && (s[index] == '-' || s[index] == '+')) {
            sign = (s[index] == '-') ? -1 : 1;
            index++;
        }

        while (index < s.size() && s[index] == '0') {
            index++;
        }

        auto isDigit = [](char c) {
            return c >= '0' && c <= '9';
        };

        long res = 0;
        while (index < s.size() && isDigit(s[index])) {
            int digit = s[index] - '0';
            if (res > (INT_MAX - digit) / 10) { 
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            res = res * 10 + digit;
            index++;
        }

        return static_cast<int>(res * sign);
    }
};
