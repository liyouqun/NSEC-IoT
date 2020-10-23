
preferences {
    section("When I touch the app turn these lights off…"){
        input "switchesoff", "capability.switch", multiple: true, required:true
    }
    section("When I touch the app turn these lights on…"){
        input "switcheson", "capability.switch", multiple: true, required:false
    }
    section("Lock theses locks...") {
        input "lock1","capability.lock", multiple: true
    }
    section("And change to this mode...") {
        input "newMode", "mode", title: "Mode?"
    }
    section("After so many seconds (optional)"){
        input "waitfor", "number", title: "Off after (default 120)", required: true
    }
}


def installed()
{
    log.debug "Installed with settings: ${settings}"
    log.debug "Current mode = ${location.mode}"
    subscribe(app, appTouch)
}


def updated()
{
    log.debug "Updated with settings: ${settings}"
    log.debug "Current mode = ${location.mode}"
    unsubscribe()
    subscribe(app, appTouch)
}

def appTouch(evt) {
    log.debug "changeMode, location.mode = $location.mode, newMode = $newMode, location.modes = $location.modes"
    if (location.mode != newMode) {
        setLocationMode(newMode)
        log.debug "Changed the mode to '${newMode}'"
    }	else {
        log.debug "New mode is the same as the old mode, leaving it be"
    }
    log.debug "appTouch: $evt"; lock1.lock(); switcheson.on();
    def delay=(waitfor != null && waitfor != "") ? waitfor * 1000 : 120000
    switchesoff.off(delay: delay)
}
