class Solution {
public:
    
    int total = 0;
    
    void DFS(TreeNode* current, int value){
        if (current == NULL){
            return;
        }
        
        if (current->left == NULL && current->right == NULL){
            total += current->val;
            total += value*10;
            return ;
        }
        
        DFS(current->left, (value*10)+current->val);
        DFS(current->right, (value*10)+current->val);  
    }
    
    int sumNumbers(TreeNode* root) {
        DFS(root, 0);
        return total;
    }
};
