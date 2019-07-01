function [F2] = compute_corr5(x_post,cut)
index = 1;
step = 50;
n1 = 20;
n2 = 20;
aug_n = 100;
len = 2500;
start_len = 100;
% you can change above parameters
for k=1:aug_n
    start = floor(start_len*k/aug_n);
    index = 1;
for i = 1:length(x_post) 
    if  length(x_post{i})==0
        display(i);
        continue; 

    end
    
    tmp2 = x_post{i}(start:start+len,:);
   
    
    len2 = size(tmp2,1);    
    
    for j=1:step:len2-cut
      
       
        s2 = tmp2(j:j+cut,1:20);        
        %s2 = mean(s2,3);            
        pc2 = corr(s2,s2);
       
        F2(index,k,round(j/step)+1,:) = pc2(:);
       
    end
   index = index+1;
end

    
end

end
