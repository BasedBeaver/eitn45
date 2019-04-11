function I=MutualInformation(P)
% The mutual information I(X;Y)
%
% P=P(X,Y) is the joint probability of X and Y.

[rownum, colnum] = size(P);

%-------%
row_v = zeros(rownum);
for i = 1:rownum;
    row_sum = 0;
    for j = 1:colnum;
        row_sum = row_sum + P(i,j);
    end
    row_v(i) = row_sum;
end

%-------%
col_v = zeros(colnum);
for i=1:colnum
      col_sum = 0;
    for j=1:rownum
        col_sum = col_sum + P(j,i);
    end
    col_v(i) = col_sum;
end

%-------%
H_x = 0;
for i = 1:rownum;
    H_x = H_x - (row_v(i) * logg2(row_v(i)));
end

%-------%
H_y = 0;
for i = 1:colnum;
    H_y = H_y - (col_v(i) * logg2(col_v(i)));
end

%-------%
H_xy = 0;
for i=1:rownum
    for j=1:colnum
        H_xy = H_xy -(P(i,j)*logg2(P(i,j)));
    end
end
I = H_x + H_y - H_xy;
end

%-------%
function x = logg2(nbr)
if nbr == 0;
    x = 0;
else
    x = log2(nbr);
end
end