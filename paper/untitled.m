N=100;
T=100000;
% nLMEM
for A=0:10;
    a=A/10;
	for n=1:N;
        % t=1ÀÏ ¶§,
        r=rand(1);
    	if r>0.5;
           s(1)=1;
        elseif r<0.5;
           s(1)=-1;
        end
        S(1)=s(1);
        squareS(1)=s(1)*s(1);
        % t>1ÀÏ ¶§,
        for t=2:T;
            r=rand(1);
            if r<1/(t^a);
               if r>1/(t^a)*0.5;
                  s(t)=1;
               elseif r<1/(t^a)*0.5;
                  s(t)=-1;
               end
            elseif r>1/(t^a);
                   s(t)=s(t-1)*(-1);
            end
            S(t)=S(t-1)+s(t);        
        end
        squareS=S.*S;   
        Y(n,:)=S;
        squareY(n,:)=squareS;
    end
    for t=1:T;
    y(t)=t^(2*0.5); % H=0.5
    meanX(t)=mean(Y(:,t));
    meansquareX(t)=mean(squareY(:,t));
    varX(t)=meansquareX(t)-meanX(t).*meanX(t);
    end
meanXX(A+1,:)=meanX;
varXX(A+1,:)=varX;
    if A+1==1;
    figure(1); loglog(1:T,varXX(A+1,:),'+b');hold on;
    elseif A+1==3;
    loglog(1:T,varXX(A+1,:),'+b');
    elseif A+1==5;
    loglog(1:T,varXX(A+1,:),'+b');
    elseif A+1==7;
    loglog(1:T,varXX(A+1,:),'+b');
    elseif A+1==9;
    loglog(1:T,varXX(A+1,:),'+b');
    end
end
fit=polyfit(log(tt),log(varXX(1,:)),1);
loglog(tt,tt.^fit(1),'-r');
xlabel('t');
ylabel('<X^2>-<X>^2');