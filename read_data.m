clear;
data_name = 30:77;
list = dir('.');
    index1 = 1;
    index2 = 1;
    index3 = 1;
    index4 = 1;
for i=1:length(data_name)
   
    fold_name = ['FN_0',int2str(data_name(i))];
    name1 =[ 'FN_0',int2str(data_name(i)),'_DRUG_V1_Resting_POST.mat'];
    name2 = ['FN_0',int2str(data_name(i)),'_DRUG_V1_Resting_POST2.mat'];
    name3 =[ 'FN_0',int2str(data_name(i)),'_DRUG_V2_Resting_POST.mat'];
    name4 = ['FN_0',int2str(data_name(i)),'_DRUG_V2_Resting_POST2.mat'];
    name5 = ['FN_0',int2str(data_name(i)),'_PLACEBO_V1_Resting_POST.mat'];
    name6 = ['FN_0',int2str(data_name(i)),'_PLACEBO_V1_Resting_POST2.mat'];
    name7 = ['FN_0',int2str(data_name(i)),'_PLACEBO_V2_Resting_POST.mat'];
    name8 = ['FN_0',int2str(data_name(i)),'_PLACEBO_V2_Resting_POST2.mat'];
    
    list = dir(['./',fold_name]);
   
    
    if length(list)>0
        
    sign = fopen(['./',fold_name,'/',name1]);
    
    if (sign)>0
        sign = load(['./',fold_name,'/',name1]);
        tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        drug_p{index1} = tmp;
        drug_name(index1)=data_name(i);
       
    end
    
    sign = fopen(['./',fold_name,'/',name2]);
    
    if (sign)>0
        sign = load(['./',fold_name,'/',name2]);
         tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        drug_p2{index1} = tmp;
        drug_name2(index1)=data_name(i);

         index1 = index1+1;
    end
    
    
    sign = fopen(['./',fold_name,'/',name3]);
    
    if (sign)>0
        sign = load(['./',fold_name,'/',name3]); tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        drug_p{index1} = tmp;
        drug_name(index1)=data_name(i);

    end
    
    sign = fopen(['./',fold_name,'./',name4]);
    
    if (sign)>0
         sign = load(['./',fold_name,'./',name4]); tmp = [];
         tmp(:,:,1)=sign.HbO;
         tmp(:,:,2)=sign.HbR;
         tmp(:,:,3)=sign.HbT;
         drug_p2{index1} = tmp;
         drug_name2(index1)=data_name(i);

           index1 = index1+1;
    end
    
    %%%%%%%%%%%%%%%%Placebo
    sign = fopen(['./',fold_name,'/',name5]);
    
    if (sign)>0
         sign = load(['./',fold_name,'/',name5]); tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        placebo{index3} = tmp;
        pl_name(index3) = data_name(i);
    end
    
    sign = fopen(['./',fold_name,'/',name6]);
    
    if (sign)>0
         sign = load(['./',fold_name,'/',name6]); tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        placebo2{index3} = tmp;
         pl_name2(index3) = data_name(i);
         index3 = index3+1;
    end
    
    sign = fopen(['./',fold_name,'/',name7]);
    
    if (sign)>0
        sign = load(['./',fold_name,'/',name7]); tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        placebo{index3} = tmp;
        pl_name(index3) =data_name(i);
    end
    
    sign = fopen(['./',fold_name,'/',name8]);
    
    if (sign)>0
        
        sign = load(['./',fold_name,'/',name8]); tmp = [];
        tmp(:,:,1)=sign.HbO;
        tmp(:,:,2)=sign.HbR;
        tmp(:,:,3)=sign.HbT;
        placebo2{index3} = tmp;
        pl_name2(index3) = data_name(i);
        index3 = index3+1;
        
     end
    
    end
end

save('matlab-data-all.mat');
