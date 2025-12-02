from fp_wrapper import solve_system

def run_case(x1_0,x2_0,tol,max_iter,scale):
  x1,x2,iters = solve_system(x1_0,x2_0,tol=tol,max_iter=max_iter,scale=scale)

def unittest():
  run_cases(0.5,0.5,tol=1e-9,max_iter=2000,scale=0.1)
  run_cases(0.5,0.5,tol=1e-9,max_iter=2000,scale=0.07)
  run_cases(0.6,0.75,tol=1e-9,max_iter=2000,scale=0.13)
  run_cases(1.0,-1.5,tol=1e-6,max_iter=2000,scale=0.3)
  run_cases(2.5,2,tol=1e-6,max_iter=2000,scale=0.35)

if _name_=="main":
  unittest()
  
