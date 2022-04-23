##########
# params #
##########
# debug the makefile?
DO_MKDBG?=0
# do doots?
DO_TOOLS:=1
# do you want dependency on the Makefile itself ?
DO_ALLDEP:=1


########
# code #
########
ALL:=
OUT:=out
TOOLS_STAMP:=$(OUT)/tools.stamp

ifeq ($(DO_MKDBG),1)
Q=
# we are not silent in this branch
else # DO_MKDBG
Q=@
#.SILENT:
endif # DO_MKDBG

ifeq ($(DO_TOOLS),1)
ALL+=$(TOOLS_STAMP)
endif # DO_TOOLS

# dependency on the makefile itself
ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif

#########
# rules #
#########
# do not add a body for this rule
.PHONY: all
all: $(ALL)
	@true

.PHONY: debug
debug:
	$(info ALL is $(ALL))

$(TOOLS_STAMP): config/deps.py
	$(info doing [$@])
	$(Q)pymakehelper touch_mkdir $@
