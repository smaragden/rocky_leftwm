targets != grep -o -E '^RPM/.*.rpm' Makefile

DOCKER_IMAGE := leftwm-rpmbuilder

all: $(targets)

.Dockerfile.timestamp: Dockerfile rpm_build.sh
	docker build --rm -t $(DOCKER_IMAGE) $(shell dirname $<)
	touch $@

RPM/dunst-1.8.1-2.el8.x86_64.rpm: specs/dunst.spec
RPM/feh-3.8-1.x86_64.rpm: specs/feh.spec
RPM/leftwm-0.2.11-1.el8.x86_64.rpm: specs/leftwm.spec
RPM/picom-9.1-1.el8.x86_64.rpm: specs/picom.spec
RPM/polybar-3.6.1-1.el8.x86_64.rpm: specs/polybar.spec
RPM/rofi-1.7.3-2.el8.x86_64.rpm: specs/rofi.spec
RPM/slock-1.4-17.el8.x86_64.rpm: specs/slock.spec
RPM/scrot-1.7-1.el8.x86_64.rpm: specs/scrot.spec

%.rpm: .Dockerfile.timestamp
	@mkdir -p RPM
	@echo $^
	docker run --rm -v $(realpath .):/host $(DOCKER_IMAGE) $(word 2,$^)

clean:
	rm -rf RPM/
	rm .Dockerfile.timestamp
