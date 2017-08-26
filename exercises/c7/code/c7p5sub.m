function vtrace = c7p1sub(M,beta,h,vinit,eta,iters)
%vtrace = c7p1sub(M,beta,h,vinit,eta,iters)
%
%This function simulates a Hopfield network using simple Euler integration.
%
% M     is the connection matrix (should be symmetric)
% beta  is the gain of the activation function (tanh by befault)
% h     is the bias
% vinit is the initial condition vector for the v's
% eta   is the timestep for the Euler integration
% iters is the number of iterations to simulate
%
% vtrace   is the v vector state of the network over time, 
%          one column per timestep in the simulation

N = size(M,1);
vtrace = zeros(N,iters);

vtrace(:,1) = vinit(:);

for i=2:iters
 vtrace(:,i)=vtrace(:,i-1) + eta*(-vtrace(:,i-1) + ...
     beta*max(M*vtrace(:,i-1) + h,0));
end

plot(vtrace(1,:),vtrace(2,:),'o',vtrace(1,:),vtrace(2,:));


